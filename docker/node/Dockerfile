FROM node:23-slim

WORKDIR /frontend

COPY /apps/frontend/package*.json ./

RUN npm install

COPY /apps/frontend .

# CMD ["npm", "run", "dev"]