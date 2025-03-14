# 1) Make the list of users, a list of who they are friends with, and a dictionary of their friendships

users = [ # id and name as a list
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), 
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)] # list of tuples

# Create the dictionary

    # Initialize the dict with empty lists for each user id
friendships = {user["id"]: [] for user in users} 
  
for i, j in friendship_pairs:  # loop over the friendship pairs to populate the dict
    friendships [i].append(j) # --> Add j as a friend to user i
    friendships [j].append(i) # --> Add i as a friend to user j


# 2) What is the average number of connections?
    # 2a) Find Total num of connections first

    def number_of_friends(user):
        """How many friends does _user_ have?"""
        user_id = user["id"] # get the user id
        friend_ids = friendships[user_id] # for the user id, grab the id of the defined friend from the friendship dict
        return len(friend_ids)
    total_connections = sum(number_of_friends(user) for user in users) # sum of all the connections

    #2b) Divide by number of users
    num_users = len(users)
    avg_connections = total_connections / num_users # average connections

# 3) What is the most connected user? (most friends)
    # 3a) sort the list of users from most to least friends 

# Create a list (user_id, number_of_friends)
    num_friends_by_id = [(user["id"], number_of_friends(user))
                        for user in users] 

# Sort the list by num of friends
    num_friends_by_id.sort(                                     # Sort the list
        key = lambda id_and_friends: id_and_friends[1],         # by num_friends
        reverse=True                                            # largest to smallest
    )

