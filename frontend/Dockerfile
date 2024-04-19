# Fase di costruzione
FROM node:14 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]