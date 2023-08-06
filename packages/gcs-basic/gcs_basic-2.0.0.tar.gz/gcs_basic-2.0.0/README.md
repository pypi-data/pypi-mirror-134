<!-- PROJECT LOGO -->
<br />

# gcs_basic_functions
Google storage basic functions


<!-- GETTING STARTED -->
## Getting Started

   ```python
   import gcs_basic
   gcs_basic.download(bucket_name, blob_path, down_path, project)
   gcs_basic.upload(bucket_name, blob_path, local_path, project)
   gcs_basic.list_blobs(bucket_name, blob_path, project)
   ```

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python python-pip
   ```sh
   sudo apt-get install python3 python-pip
   #or
   sudo pacman -S python python-pip
   ```
* Google cloud SDK for credentials - temporarily
   ```
   wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-364.0.0-linux-x86_64.tar.gz
   tar -xvf google-cloud-sdk-364.0.0-linux-x86_64.tar.gz
   cd google-cloud-sdk-364.0.0-linux-x86_64
   bash google-cloud-sdk/install.sh
   #open new terminal
   gcloud init
   gcloud auth application-default login
   ```
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/antonio258/gcs_basic_functions.git
   ```
2. Install package
   ```sh
   cd gcs_basic_functions
   pip install .
   ```


<!-- ROADMAP -->
## Roadmap

- [x] Download one file from storage
- [x] Upload one file to storage
- [x] Download folder from storage
- [x] Upload folder to storage
- [x] List blobs
- [ ] Check credentials in library
