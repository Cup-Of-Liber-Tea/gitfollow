from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from github import Github
import os

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['your-email@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def auto_follow_back():
    # GitHub 토큰으로 인증
    github_token = os.getenv('GITHUB_ACCESS_TOKEN')
    g = Github(github_token)
    
    # 자신의 계정 정보 가져오기
    user = g.get_user()
    
    # 현재 팔로워 목록 가져오기
    followers = set(follower.login for follower in user.get_followers())
    
    # 현재 팔로잉 목록 가져오기
    following = set(following.login for following in user.get_following())
    
    # 팔로우하지 않은 팔로워 찾기
    users_to_follow = followers - following
    
    # 팔로우하지 않은 사용자들 자동 팔로우
    for username in users_to_follow:
        try:
            user_to_follow = g.get_user(username)
            user.add_to_following(user_to_follow)
            print("Successfully followed {}".format(username))
        except Exception as e:
            print("Failed to follow {}: {}".format(username, str(e)))

with DAG(
    'github_auto_follow',
    default_args=default_args,
    description='DAG to automatically follow GitHub followers',
    schedule_interval='@daily',
    catchup=False
) as dag:

    follow_task = PythonOperator(
        task_id='auto_follow_back',
        python_callable=auto_follow_back,
    )

    follow_task 