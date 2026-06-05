import logging
import subprocess

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Started")

subprocess.run(["python", "scripts/extract.py"])
logging.info("Extract Completed")

subprocess.run(["python", "scripts/transform.py"])
logging.info("Transform Completed")

subprocess.run(["python", "scripts/load.py"])
logging.info("Load Completed")

logging.info("ETL Pipeline Completed Successfully")

print("ETL Pipeline Completed Successfully")