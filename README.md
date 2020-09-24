## A repo to try out DVC

<br>

## Objectives:
The code attempts to do the following:
1. Load some data (csv and images) using a script
2. Use DVC/git to track changes to the data
3. Connect to S3 remote storage
4. Push the local images to S3 remote storage
   
<br>

### Additional Notes for multiple S3 accounts:
When using multiple S3 profiles, setup different profiles in the following files 
- ~/.aws/credentials 
- ~/.aws/config

Set in terminal before using dvc push: <br>
```export AWS_PROFILE=personal ```

<br>
<br>

#### Sources:
- [Data Version Control](https://dvc.org/)
- [DVC Github](https://github.com/iterative/dvc)


