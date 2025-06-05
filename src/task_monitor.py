name: Notion Task Monitor

on:
  schedule:
    # 15分おきに実行 (UTC時間)
    - cron: '*/15 * * * *'
  
  # 手動実行も可能
  workflow_dispatch:

jobs:
  monitor-tasks:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run task monitor
      env:
        NOTION_TOKEN: ${{ secrets.NOTION_TOKEN }}
        TASK_DATABASE_ID: ${{ secrets.TASK_DATABASE_ID }}
        HISTORY_DATABASE_ID: ${{ secrets.HISTORY_DATABASE_ID }}
      run: |
        python src/task_monitor.py
