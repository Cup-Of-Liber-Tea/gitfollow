import os
from github import Github

def test_github_follow():
    # GitHub 토큰 설정
    github_token = os.getenv('GITHUB_ACCESS_TOKEN')
    if not github_token:
        raise ValueError("GITHUB_ACCESS_TOKEN이 설정되지 않았습니다.")
    
    try:
        # GitHub API 연결 테스트
        g = Github(github_token)
        user = g.get_user()
        print(f"현재 로그인된 사용자: {user.login}")
        
        # 팔로워 목록 테스트
        print("\n현재 팔로워 목록:")
        followers = list(user.get_followers())
        for follower in followers[:5]:  # 처음 5명만 출력
            print(f"- {follower.login}")
        print(f"총 팔로워 수: {len(followers)}")
        
        # 팔로잉 목록 테스트
        print("\n현재 팔로잉 목록:")
        following = list(user.get_following())
        for follow in following[:5]:  # 처음 5명만 출력
            print(f"- {follow.login}")
        print(f"총 팔로잉 수: {len(following)}")
        
        # 팔로우 해야할 사용자 확인
        followers_set = set(f.login for f in followers)
        following_set = set(f.login for f in following)
        to_follow = followers_set - following_set
        
        print("\n팔로우 해야할 사용자:")
        for username in to_follow:
            print(f"- {username}")
            
    except Exception as e:
        print(f"에러 발생: {str(e)}")

if __name__ == "__main__":
    test_github_follow() 