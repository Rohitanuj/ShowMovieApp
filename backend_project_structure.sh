#!/usr/bin/env bash
set -e

PROJECT_ROOT="backend"
APP_DIR="$PROJECT_ROOT/app"

echo "Creating backend project skeleton..."

# Create directories
mkdir -p $APP_DIR/core
mkdir -p $APP_DIR/db/migrations
mkdir -p $APP_DIR/db/models
mkdir -p $APP_DIR/db/repositories
mkdir -p $APP_DIR/schemas
mkdir -p $APP_DIR/services
mkdir -p $APP_DIR/api/v1
mkdir -p $APP_DIR/utils
mkdir -p $APP_DIR/middleware
mkdir -p $PROJECT_ROOT/tests

# Touch empty files
touch $APP_DIR/__init__.py
touch $APP_DIR/main.py

# Core
touch $APP_DIR/core/{config.py,security.py,logging.py}

# DB
touch $APP_DIR/db/{base.py,__init__.py}
touch $APP_DIR/db/models/{__init__.py,user.py,entry.py,approval_log.py}
touch $APP_DIR/db/repositories/{__init__.py,user_repo.py,entry_repo.py,approval_repo.py}

# Schemas
touch $APP_DIR/schemas/{__init__.py,auth.py,user.py,entry.py,approval.py}

# Services
touch $APP_DIR/services/{__init__.py,auth_service.py,entry_service.py,approval_service.py}

# API
touch $APP_DIR/api/{__init__.py,deps.py}
touch $APP_DIR/api/v1/{__init__.py,auth.py,entries.py,admin.py,uploads.py}

# Utils
touch $APP_DIR/utils/{__init__.py,s3.py,image.py}

# Middleware
touch $APP_DIR/middleware/{__init__.py,error_handlers.py,rate_limit.py}

# Root level
touch $PROJECT_ROOT/{Dockerfile,pyproject.toml,requirements.txt}
touch docker-compose.yml
touch .env.example
touch README.md

echo "✅ Backend project structure created."

