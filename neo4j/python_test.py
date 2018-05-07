from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j","test"))

#

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











