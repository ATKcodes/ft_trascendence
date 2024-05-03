# Use the Nginx image from Docker Hub as the base image
FROM nginx:alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the HTML file to the Nginx document root
COPY *.html /usr/share/nginx/html

# Copy the CSS file to the Nginx document root
COPY styles.css /usr/share/nginx/html

# Copy a configuration file from the current directory
COPY nginx.conf /etc/nginx/conf.d

# Expose port 80
EXPOSE 80

# Start Nginx when the container has provisioned
CMD ["nginx", "-g", "daemon off;"]