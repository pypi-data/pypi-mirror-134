## 修改版本





clear build



python2 setup.py clean 

python2 setup.py bdist_wheel   

python2 setup.py sdist  





修改setup.py版本号

```
python2 setup.py clean 
python2 setup.py bdist_wheel sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

```





[这！就是内部pypi (alibaba-inc.com)](https://ata.alibaba-inc.com/articles/116255?spm=ata.25287382.0.0.6b937536L4gehx)