#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Qin Xuye <qin@qinxuye.me>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on 2013-5-23

@author: Chine
'''

import multiprocessing
import threading

from cola.core.mq.node import MessageQueueNodeProxy
from cola.core.mq.client import MessageQueueClient
from cola.core.utils import get_rpc_prefix, \
                            pickle_connection, unpickle_connection

PUT, PUT_INC, GET, GET_INC, EXIST = range(5)

MessageQueueClient = MessageQueueClient

class MessageQueue(MessageQueueNodeProxy):
    def __init__(self, working_dir, rpc_server, addr, addrs, 
                 app_name=None, copies=1, n_priorities=3,
                 deduper=None):
        super(MessageQueue, self).__init__(working_dir, rpc_server, addr, addrs,
                                           copies=copies, n_priorities=n_priorities,
                                           deduper=deduper, app_name=app_name)
        
        self.stopped = multiprocessing.Event()
        self.agents = []
        self.threads = []
        self.clients = {}
        
    def new_connection(self, k):
        if k in self.clients: return self.clients[k]
        
        agent, client = multiprocessing.Pipe()
        self.agents.append(agent)
        _t = threading.Thread(target=self._init_process, args=(agent,))
        self.threads.append(_t)
        _t.start()
        
        self.clients[k] = client
        return client
    
    def _init_process(self, agent):
        while not self.stopped.is_set():
            need_process = agent.poll(10)
            if self.stopped.is_set():
                return
            if not need_process:
                continue
            
            action, data = agent.recv()
            if action == PUT:
                objs, flush = data
                self.put(objs, flush=flush)
                agent.send(1)
            elif action == PUT_INC:
                self.put_inc(data)
                agent.send(1)
            elif action == GET:
                size, priority = data
                agent.send(self.get(size=size, 
                                    priority=priority))
            elif action == GET_INC:
                agent.send(self.get_inc(data))
            elif action == EXIST:
                if not self.mq_node.deduper:
                    agent.send(False)
                else:
                    agent.send(self.exist(str(data)))
            else:
                raise ValueError('mq client can only put, put_inc, and get')
            
    def _join(self):
        [t.join() for t in self.threads]
            
    def shutdown(self):
        super(MessageQueue, self).shutdown()
        self.stopped.set()
        self._join()
        [agent.close() for agent in self.agents]
        
class MpMessageQueueClient(object):
    def __init__(self, conn):
        self.conn = conn
        
    def put(self, objs, flush=False):
        self.conn.send((PUT, (objs, flush)))
        self.conn.recv()
        
    def put_inc(self, objs):
        self.conn.send((PUT_INC, objs))
        self.conn.recv()
        
    def get(self, size=1, priority=0):
        self.conn.send((GET, (size, priority)))
        return self.conn.recv()
    
    def get_inc(self, size=1):
        self.conn.send((GET_INC, size))
        return self.conn.recv()
    
    def exist(self, obj):
        self.conn.send((EXIST, str(obj)))
        return self.conn.recv()