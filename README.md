### What is this? 

This is a quick-n-dirty script that uses Selenium, in a headless fashion, to log into OpenStack's Horizon's UI and pull back the 'Usage' CSV, for integration into any analytics or accounting packages you might need to use this data with. 

### Why do I need to use a browser? 

The data in the 'Usage' output, is not the same as `openstack usage list` from the CLI/API. One produces data relevant to the overall _consumption_ of the cluster, while the other prouduces data on the overall _usage_ of the cluster, over time. 

They're distinctly different, and there doesn't appear to be a way to get at the usage data found in Horizon, through the API. There may be a way to construct a direct MySQL query to union the data, but it's not obvious, so... I created this script. 

### How do I run this? 

Easy-peasey! 

1. Create a virtual environment: 

    ``` bash 
    python3 -m venv env
    ```
2. Source that environment: 
    ``` bash 
    . env/bin/activate
    ```
3. Install selenium and dependencies: 
    ``` bash 
    pip install selenium 
    ```
4. Update the username/password/domain at the top of the file, or you can uncomment the relevant section and have it prompt you for those credentials. 

    This intentionally does not store those credentials anywhere on the filesystem, other than those defined in this file. 
5. That's it! 

### Credits

- OpenStack, for making this monstrous project with so many moving parts.