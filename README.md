# Trading Agents

前後端分離嘅 Trading Agents 專案：Backend API（FastAPI + LangChain）配 Next.js 前端。

## 技術棧

- **Backend**：Python 3.11+、FastAPI、LangChain、DeepSeek、uvicorn；套件管理用 **uv**
- **Frontend**：Next.js 16、React 19、TypeScript、Tailwind；套件管理用 **yarn**

## 編程風格

前後端都以 **函數式編程** 為主：純函數、少可變狀態、組合優於繼承；Backend 用純函數處理業務邏輯，Frontend 用函數組件與 custom hooks，避免 class component 與隱藏副作用。詳見 [.cursor/rules/functional-programming.mdc](.cursor/rules/functional-programming.mdc)。

## 前置需求

- [Python 3.11+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/)（Backend 依賴管理）
- [Node.js](https://nodejs.org/)
- [yarn](https://yarnpkg.com/)（Frontend 依賴管理）

## 目錄結構

| 目錄 | 職責 |
|------|------|
| `backend/` | FastAPI API、LangChain 邏輯，用 uv 管理 Python 依賴 |
| `frontend/` | Next.js 應用，用 yarn 管理 Node 依賴 |

## 架構示意

```mermaid
flowchart LR
  subgraph repo [tradingAgents]
    backend[backend uv FastAPI]
    frontend[frontend yarn Next.js]
  end
  frontend -->|HTTP API| backend
  backend -->|/docs| apiDocs[OpenAPI]
```

## 環境變數

環境變數請參考專案根目錄 [.env.example](.env.example)。複製為根目錄 `.env` 後填入（Docker Compose 同本地跑 backend 都會用呢個檔）：

- `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB`（Postgres）
- `DATABASE_URL`（本機開發用 `localhost:5432`；Docker 會自動 override 為 `db:5432`）
- `OPENAI_API_KEY`、`DEEPSEEK_API_KEY`（如使用）

## 安裝與執行

### Backend

```bash
cd backend
uv sync
uv run main.py
```

或：`uv run python main.py`。API 預設喺 `http://0.0.0.0:8000`。

### Frontend

```bash
cd frontend
yarn
yarn dev
```

開發伺服器預設喺 [http://localhost:3000](http://localhost:3000)。建置與生產啟動：`yarn build`、`yarn start`。

## UAT / PROD 同機部署

同一部機可同時跑 UAT 同 PROD，靠唔同 Compose project 名同 env file 隔離。

1. **準備 env 檔**：複製 `.env.uat.example` → `.env.uat`、`.env.prod.example` → `.env.prod`，分別填入唔同嘅 DB 名、port、密碼（兩邊唔共用同一個 DB 同密碼）。
2. **啟動**：
   - UAT：`docker compose -p trading-agents-uat --env-file .env.uat up -d`
   - PROD：`docker compose -p trading-agents-prod --env-file .env.prod up -d`
3. **停止**：`docker compose -p trading-agents-uat down` / `docker compose -p trading-agents-prod down`

兩邊 DB 同 volume 會自動隔離（`uat_postgres_data`、`prod_postgres_data`），port 由各 env file 嘅 `PORT_*` 決定（UAT 預設 5433/8001/3001，PROD 預設 5432/8000/3000）。

## API 文件

Backend 啟動後可訪問：

- **Swagger UI**：`http://localhost:8000/docs`
- **ReDoc**：`http://localhost:8000/redoc`
