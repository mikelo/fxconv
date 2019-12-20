# standard installation:
```python
pip3 install --user flask
export FLASK_APP=backend.py
export FLASK_ENV=development
flask run
```
test URL http://127.0.0.1:5000/convert?amount=2.2&src%E2%80%8B_currency=AUD&dest%E2%80%8B_currency=BRL&re%E2%80%8Bference_date=2019-12-19


# docker installation:
```bash
sudo docker build -t fxconv .
sudo docker run --net host --rm -it fxconv
```
