# Put the use case you chose here. Then justify your database choice:
#
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
#
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
#
#



# Action 1: <create an account>
# Create a person node.
def _create_and_return_account(tx, username):
    result = tx.run("CREATE (a:Account) "
                    "SET a.username = $username "
                    "RETURN a.username + ', from node ' + id(a)", username=username)
    stuff = result.single()[0]
    print(stuff)



@classmethod
def create_user(cls, tx, name):
    tx.run("CREATE (:Account {name: $name})", name=name)




def create_follow(cls, tx, name_a, name_b):
    tx.run("MATCH (a:User {name: $name_a}) "
           "MATCH (b:User {name: $name_b}) "
           "MERGE (a)-[:FOLLOWS]->(b)",
           name_a=name_a, name_b=name_b)


def print_friendships(cls, tx):
    result = tx.run("MATCH (a)-[:KNOWS]->(b) RETURN a.name, b.name")
    for record in result:
        print("{} follows {}".format(record["a.name"] ,record["b.name"]))

print("hello")

# Action 2: <describe the action here>


# Action 3: <describe the action here>


# Action 4: <describe the action here>


# Action 5: <describe the action here>


# Action 6: <describe the action here>


# Action 7: <describe the action here>


# Action 8: <describe the action here>



