FROM node:lts-alpine 
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build