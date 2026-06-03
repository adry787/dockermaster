#!/usr/bin/env python3
import docker
class Manager:
    def __init__(self): self.c = docker.from_env()
    def list(self): return [{"id":c.short_id,"name":c.name,"status":c.status} for c in self.c.containers.list(all=True)]
    def start(self,name): self.c.containers.get(name).start(); return f"Started {name}"
    def stop(self,name): self.c.containers.get(name).stop(); return f"Stopped {name}"
if __name__=="__main__":
    import sys; m=Manager()
    if len(sys.argv)<2: print("Usage: manage.py list|start|stop <name>"); exit()
    cmd=sys.argv[1]
    if cmd=="list":
        for c in m.list(): print(f"{c['id']} {c['name']:20s} {c['status']}")
    elif cmd=="start" and len(sys.argv)>2: print(m.start(sys.argv[2]))
    elif cmd=="stop" and len(sys.argv)>2: print(m.stop(sys.argv[2]))
