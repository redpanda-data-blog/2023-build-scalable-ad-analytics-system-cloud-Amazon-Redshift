# How to integrate Redpanda and AWS-Redshift

This repository contains the resources and instructions for deploying a scalable ad analytics system leveraging Redpanda and AWS Redshift. The system aims to provide real-time insights into advertising data, crucial for optimizing ad campaigns.

## Overview

The project integrates Redpanda, an Apache Kafka–compatible event streaming platform, with AWS Redshift, a fully managed, petabyte-scale data warehouse service. The integration facilitates the ingestion, storage, and analysis of large-scale ad data, providing vital insights into ad performance metrics like impressions, clicks, conversions, and more.

## System Architecture

![Architecture Diagram](https://i.imgur.com/aN1sOlB.png)

The architecture showcases the workflow from data generation to insights retrieval. The system ingests streaming ad data into Redpanda, transfers it to AWS Redshift via a JDBC Sink Connector, and then performs analytics queries on the data.

## Prerequisites

- Python 3.11+
- Docker 24.0.6+
- AWS Account with Redshift

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [your-repo-link]
   cd [your-repo-name]
   ```

2. **Virtual Environment:**
   - Create and activate a Python virtual environment.

3. **Docker Setup:**
   - Ensure Docker is installed and running on your machine.

4. **Redpanda Setup:**
   - Follow instructions to run Redpanda in a Docker container.

5. **AWS Redshift Account:**
   - Set up an AWS Redshift account as per the provided instructions.

## Usage

1. **Generate Synthetic Data:**
   - Run `python generate_data.py` to create a synthetic dataset of ad events.

2. **Produce Data to Redpanda Topic:**
   - Execute `python produce_data.py` to send data to the Redpanda topic.

3. **Setup Kafka Connect for Redshift:**
   - Configure Kafka Connect with Redpanda and set up the JDBC Sink Connector for AWS Redshift.

4. **Start Data Transfer:**
   - Run the Kafka Connector to begin transferring data from Redpanda to AWS Redshift.

5. **Querying in AWS Redshift:**
   - Access the Redshift Query Editor to perform SQL queries on the ingested data.

