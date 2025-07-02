

import requests



def get_profile_info(username):
            
    url = "https://leetcode.com/graphql"

    query = """
        query getUserProfile($username: String!){
            matchedUser(username : $username){
                username
                profile {
                    ranking
                    reputation
                }

                submitStats {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }

            }
        }
    """



    variables = {"username":username}

    headers = {
        "Content-Type":"application/json",
        "Referer":f"https://leetcode.com/u/{username}/",
        "User-agent":"Mozilla/5.0"
    }

    res = requests.get(url, json={"query":query, "variables":variables}, headers=headers)

    data = res.json()


    if not data.get("data") or not data["data"].get("matchedUser"):
        print("Username does not found")
        return

    user_data = data["data"]["matchedUser"]
    # badges = data["data"]["matchedUser"]["badges"]
    stats = user_data["submitStats"]["acSubmissionNum"]

    profile = {
        "username":user_data["username"],
        "ranking":user_data["profile"]["ranking"],
        "easy":stats[1]["count"],
        "medium":stats[2]["count"],
        "hard":stats[3]["count"],
        "total":stats[0]["count"]
    }
    return profile

