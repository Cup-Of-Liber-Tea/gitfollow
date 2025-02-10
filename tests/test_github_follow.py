# -*- coding: utf-8 -*-
import os
from github import Github

def test_github_follow():
    # GitHub 토큰 직접 설정
    github_token = '?'
    
    try:
        # GitHub API 연결 테스트
        g = Github(github_token)
        user = g.get_user()
        print("Currently logged in user: {}".format(user.login))
        
        # 팔로워 목록 테스트
        print("\nCurrent followers list:")
        followers = list(user.get_followers())
        for follower in followers[:5]:  # 처음 5명만 출력
            print("- {}".format(follower.login))
        print("Total followers: {}".format(len(followers)))
        
        # 팔로잉 목록 테스트
        print("\nCurrent following list:")
        following = list(user.get_following())
        for follow in following[:5]:  # 처음 5명만 출력
            print("- {}".format(follow.login))
        print("Total following: {}".format(len(following)))
        
        # 팔로우 해야할 사용자 확인
        followers_set = set(f.login for f in followers)
        following_set = set(f.login for f in following)
        to_follow = followers_set - following_set
        
        print("\nUsers to follow:")
        for username in to_follow:
            print("- {}".format(username))
            
    except Exception as e:
        print("Error occurred: {}".format(str(e)))

if __name__ == "__main__":
    test_github_follow() 