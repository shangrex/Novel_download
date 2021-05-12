# novel_download
for fun
* wenku
* ptt
* piaotian

## Setup environment
* clone to the local
    ```
    git clone https://github.com/shangrex/Novel_download.git
    ```
* open the virtual enviroment
    ```
    pipenv shell
    ```
* download the package
    ```
    pipenv install --dev
    ```

    
## piaotian_list
* description:
    Download each novel first pages and build the csv data
* target web page
    ![](https://i.imgur.com/sROPaxM.png)

* data format
    ![](https://i.imgur.com/fGPU6dK.png)
* running screen
    ![](https://i.imgur.com/IwE6Vh4.png)

* command
    ```
    pipenv run piaotian
    ```

## mingyan_list
* description:
    download the motto from minyangtong

* target webpage
    ![](https://i.imgur.com/WvNr7YG.png)

* data format


* running screen

* command
    ```
    pipenv run mingyan
    ```
* warning
    every webcrawl has 10 sec sleep time