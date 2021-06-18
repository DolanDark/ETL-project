from neo4j import GraphDatabase
from datetime import datetime
import os

now = datetime.now()
t_val = now.strftime("%H:%M:%S")        #was not used, kept for reference
print(t_val)

graphdb=GraphDatabase.driver(uri="bolt://localhost:7687", auth=("ron", "ronny"))        #please change credentials as per your db's

print(graphdb)
session = graphdb.session()


query1 = '''
CALL apoc.load.json("file:/user_data.json") yield value
unwind value.a1.usages as u
unwind value.a1.device as d
MERGE (usr:User {user_id:value.a1.user_id})
MERGE (ap:App {app_name:u.app_name, app_category:u.app_category})
MERGE (dev:Device {os:d.os})
MERGE (br:Brand {brand:d.brand})
MERGE (usr)-[r1:USED {time_created:time(), time_event: value.a1.usages_date, usage_minutes: u.minutes_used}]->(ap)-[r2:ON {time_created:time()}]->(dev)-[r3:OFF {time_created:time()}]->(br)
'''

query2 = '''
CALL apoc.load.json("file:/user_data.json") yield value
unwind value.a2.usages as u
unwind value.a2.device as d
MERGE (usr:User {user_id:value.a2.user_id})
MERGE (ap:App {app_name:u.app_name, app_category:u.app_category})
MERGE (dev:Device {os:d.os})
MERGE (br:Brand {brand:d.brand})
MERGE (usr)-[r1:USED {time_created:time(), time_event: value.a2.usages_date, usage_minutes: u.minutes_used}]->(ap)-[r2:ON {time_created:time()}]->(dev)-[r3:OFF {time_created:time()}]->(br)
'''

query3 = '''
CALL apoc.load.json("file:/user_data.json") yield value
unwind value.a3.usages as u
unwind value.a3.device as d
MERGE (usr:User {user_id:value.a3.user_id})
MERGE (ap:App {app_name:u.app_name, app_category:u.app_category})
MERGE (dev:Device {os:d.os})
MERGE (br:Brand {brand:d.brand})
MERGE (usr)-[r1:USED {time_created:time(), time_event: value.a3.usages_date, usage_minutes: u.minutes_used}]->(ap)-[r2:ON {time_created:time()}]->(dev)-[r3:OFF {time_created:time()}]->(br)
'''

query4 = '''
CALL apoc.load.json("file:/user_data.json") yield value
unwind value.a4.usages as u
unwind value.a4.device as d
MERGE (usr:User {user_id:value.a4.user_id})
MERGE (ap:App {app_name:u.app_name, app_category:u.app_category})
MERGE (dev:Device {os:d.os})
MERGE (br:Brand {brand:d.brand})
MERGE (usr)-[r1:USED {time_created:time(), time_event: value.a4.usages_date, usage_minutes: u.minutes_used}]->(ap)-[r2:ON {time_created:time()}]->(dev)-[r3:OFF {time_created:time()}]->(br)
'''

query5 = '''
CALL apoc.load.json("file:/user_data.json") yield value
unwind value.a5.usages as u
unwind value.a5.device as d
MERGE (usr:User {user_id:value.a5.user_id})
MERGE (ap:App {app_name:u.app_name, app_category:u.app_category})
MERGE (dev:Device {os:d.os})
MERGE (br:Brand {brand:d.brand})
MERGE (usr)-[r1:USED {time_created:time(), time_event: value.a5.usages_date, usage_minutes: u.minutes_used}]->(ap)-[r2:ON {time_created:time()}]->(dev)-[r3:OFF {time_created:time()}]->(br)
'''

session.run(query1)
session.run(query2)
session.run(query3)
session.run(query4)
session.run(query5)