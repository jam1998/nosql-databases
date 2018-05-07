from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j","test"))




# Put the use case you chose here. Then justify your database choice:
# I chose to  model the Application Instagram using the database neo4j. The reason I chose Neo4j was for its conveience in extracting and 
# forming relationships between entities in some given data. There is no need to use map reduce or analytics to extract information about 
# relationships between entities. Neo4j gives you the possibility to identify clusters in the data, answer questions, provide insights.
# The scalibility and flexibility that Neo4j offers for a program like Instagram powered by the immense ease in which it is able to establslish relationships 
# on the countless amounts of data being poured in is why I chose this database.


# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.

# If coffee is spilled on one of the servers causing it to go down. As many noSql databases use the master-slave relation we can still expect it to be functional. 
# The neo4j documentation states that a key feature of neo4j is it's high availability. That is, even in the presence of failures, the system continues
# to deliver it functionality to end user including humans or other computer system. Neo4j's clustering architecture is an automated soulution for ensuring that Neo4j is
# continuously available. The premise is that we deploy redundancy into the cluster such that if failures occur they can be masked by the remaining live instances. 
# In the case above a single failed instance does not cause the cluster to stop (though the throughput of the cluster may be lower). Neo4j documentation then states that
# In these cases a disaster recovery strategy can define a failover datacenter along with a strategy for bringing services back online. Neo4j clustering can accommodate disaster 
# recovery strategies that require very short-windows of downtime or low tolerances for data loss in disaster scenarios. By deploying a cluster instance to an alternate location,
# you have an active copy of your database up and available in your designated disaster recovery location that is up to date with the transactions executed against your operational 
# database cluster. So it seems that in the event of a coffee disaster we can expect our information to preserves and for application using the server to remain functional.

# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?

# The data that is absolutely not okay for my application to loose includes personal information of the user such as
# name and date of birth. It is crucial that any financial information such as banking information or transaction information
# or monetary revenue of a post on my application to be preserved and available.  We can also imagine that uploading photo or
# inserting post data is far more crucial than data involving liking a photo. While we would like to lose information regarding
# a post it is likely acceptable to delay how quickly a post can be viewed by other. On the other seeing  and sending a message
# immediately is very critical as otherwise not be an enjoyable messaging platform. To mitigate the loss of data in our commands
# we can take several steps. These steps include making the data asynchronous as well as preventing any ambiguity on the
# identifying markers of any piece of data. We can also make sure the commands in our code establish comprehendable relationships
# as well as contain features that prevent it from being accidentally mutated by a user. We can also make sure that
# there are atomic operations or transactions throughout the code. 







def delete_graphs():
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (n) DETACH DELETE n ")
delete_graphs()

#

def create_user(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            result = tx.run("CREATE (a:User) "
                        "SET a.name = $name "
                        "RETURN a.name + ', from node ' + id(a)", name=name)
        print(result.single()[0])

create_user("Herman Lay")
create_user("Phil Knight")
create_user("Charles Alderton")

#
#

def create_account(username):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            result = tx.run("CREATE (a:Account) "
                        "SET a.username = $username "
                        "RETURN a.username + ', from node ' + id(a)", username=username)
        print(result.single()[0])


create_account("Lay's-Chips")
create_account("Wise-Chips")
create_account("Nike")
create_account("Jordans")
create_account("Snapple-Group")
create_account("Pepsi-Group")


#

def create_post(title):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            result = tx.run("CREATE (a:Post) "
                        "SET a.title = $title "
                        "RETURN a.title + ', from node ' + id(a)", title=title)
        print(result.single()[0])

create_post("Lays")
create_post("Cheetos")
create_post("Sun-Chips")
create_post("Tostitos")
create_post("Crush")
create_post("Retros")
create_post("Uptowns")
create_post("7-Up")
create_post("Dr.Pepper")


#


def create_ownership(name_a, username_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:User {name: $name_a}) "
                   "MATCH (b:Account {username: $username_b}) "
                   "MERGE (a)-[:OWNS]->(b)",
                   name_a=name_a, username_b=username_b)

create_ownership("Herman Lay","Lay's-Chips")
create_ownership("Herman Lay","Wise-Chips")
create_ownership("Phil Knight","Nike")
create_ownership("Phil Knight","Jordans")
create_ownership("Charles Alderton","Snapple-Group")
create_ownership("Charles Alderton","Pepsi-Group")

#

def create_post_ownership(username_a, title_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Post {title: $title_b}) "
                   "MERGE (a)-[:POSTED]->(b)",
                   username_a=username_a, title_b=title_b)


create_post_ownership("Lay's-Chips","Lays")
create_post_ownership("Lay's-Chips","Cheetos")
create_post_ownership("Wise-Chips","Sun-Chips")
create_post_ownership("Wise-Chips","Tostitos")
create_post_ownership("Nike","Uptowns")
create_post_ownership("Jordans","Retros")
create_post_ownership("Snapple-Group","Dr.Pepper")
create_post_ownership("Pepsi-Group","7-Up")
create_post_ownership("Pepsi-Group","Crush")


#




#
def print_ownership_of(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:User)-[:OWNS]->(b:Account) "
                                 "WHERE a.name = {name} "
                                 "RETURN b.username", name=name):
                print(record["b.username"])

print_ownership_of("Herman Lay")
print_ownership_of("Phil Knight")
print_ownership_of("Charles Alderton")



#

def print_posts_of(username):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:Account)-[:POSTED]->(b:Post) "
                                 "WHERE a.username = {username} "
                                 "RETURN b.title", username=username):
                print(record["b.title"])


print_posts_of("Lay's-Chips")
print_posts_of("Wise-Chips")
print_posts_of("Nike")
print_posts_of("Jordans")
print_posts_of("Snapple-Group")
print_posts_of("Pepsi-Group")








#My user story is on how different companies use social media to promote products and it is not meant to be a linear story line
# Action 1: <Snapple-Group Likes one of its posts>
def leave_like(username_a, title_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Post {title: $title_b}) "
                   "MERGE (a)-[:LIKES]->(b)",
                   username_a=username_a, title_b=title_b)
leave_like("Snapple-Group","Dr.Pepper")          

# Action 2: <User Messages another User>

def send_message(username_a, username_b,message_c):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Account {username: $username_b}) "
                   "MERGE (a)-[:MESSAGE{MESSAGE_1:$message_c}]->(b)",
                   username_a=username_a, username_b=username_b, message_c=message_c)

send_message("Snapple-Group","Pepsi-Group","We are better than you")

# Action 3: <User Makes Comment>
def make_comment(username_a, title_b,comment_c):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Post {title: $title_b}) "
                   "MERGE (a)-[:COMMENT{MESSAGE:$comment_c}]->(b)",
                   username_a=username_a, title_b=title_b, comment_c=comment_c)

make_comment("Lay's-Chips","Lays","We are Yummy")


# Action 4: <A user follows another user>
def create_follow(username_a, username_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Account {username: $username_b}) "
                   "MERGE (a)-[:FOLLOWS]->(b)",
                   username_a=username_a, username_b=username_b)
create_follow("Lay's-Chips", "Nike")          

# Action 5: <A user sees all their followers>
def print_follows_of(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:Account)-[:FOLLOWS]->(b:Account) "
                                 "WHERE a.username = {name} "
                                 "RETURN b.username", name=name):

                print(record["b.username"])

print_follows_of("Lay's-Chips")             


# Action 6: <User requests money from another User>
def money_request(username_a, username_b, money_c):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Account {username: $username_b}) "
                   "MERGE (a)-[:REQUESTS{AMOUNT:$money_c}]->(b)",
                   username_a=username_a, username_b=username_b, money_c=money_c)
money_request("Jordans", "Nike","42.00") 



# Action 7: <User posts a video>
def create_video(video_title):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            result = tx.run("CREATE (a:Video) "
                        "SET a.video_title = $video_title "
                        "RETURN a.video_title + ', from node ' + id(a)", video_title=video_title)
        print(result.single()[0])
create_video("Watch Me")

def create_video_ownership(username_a, video_title_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Video {video_title: $video_title_b}) "
                   "MERGE (a)-[:POSTED_VIDEO]->(b)",
                   username_a=username_a, video_title_b=video_title_b)

create_video_ownership("Jordans","Watch Me")


# Action 8: <User places an advertisement>
def create_ad(title):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            result = tx.run("CREATE (a:Advertisement) "
                        "SET a.title = $title "
                        "RETURN a.title + ', from node ' + id(a)", title=title)
        print(result.single()[0])
create_ad("Buy My Shoes")


def create_ad_ownership(username_a, title_b):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            tx.run("MATCH (a:Account {username: $username_a}) "
                   "MATCH (b:Advertisement {title: $title_b}) "
                   "MERGE (a)-[:ADVERTISED]->(b)",
                   username_a=username_a, title_b=title_b)
create_ad_ownership("Nike","Buy My Shoes")

