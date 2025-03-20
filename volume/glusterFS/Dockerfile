# Use an Ubuntu base image
FROM ubuntu:20.04

# Set non-interactive mode for apt-get to avoid any prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install prerequisites
RUN apt-get update && \
    apt-get install -y software-properties-common curl && \
    apt-get clean

# Add the GlusterFS PPA repository
RUN add-apt-repository ppa:gluster/glusterfs-10

# Update apt repositories
RUN apt-get update

# Install GlusterFS server
RUN apt-get install -y glusterfs-server

# Expose ports for GlusterFS if required
EXPOSE 24007 24008 24009 24010

# Set up GlusterFS as the default command (no need to use systemctl in Docker)
CMD ["glusterd", "-N"]
