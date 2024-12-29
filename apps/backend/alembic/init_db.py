import sys
import os

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config.database import init_db

async def asyn_init_db():
    # データベースの初期化
    await init_db()

if __name__ == "__main__":
    asyn_init_db()