# Caching **Rateflex**

Rateflex is a lightweight Python-based app that serves as a proxy to support developers working with rate-limited third-party APIs. It allows developers to program against these APIs without being hindered by rate limitations. Rateflex intercepts all requests and either responds with cached data or forwards the request to the target host if it hasn't been previously cached.

## Running Rateflex
### Docker
The easiest way to get started with Rateflex is by using the prebuilt Docker image. Use the following command to start the app on port 5000:
```shell
docker run -p "5000:5000" neilblaze/rateflex
```

If you want to use a local session file you must mount it to the container:
```shell
docker run -p "5000:5000" -v "/tmp/cache.session:/cache.session" neilblaze/rateflex
```

### From source
You can also run Rateflex from the source code. After cloning the repository on local, install the required dependencies:
```shell
pip install -r requirements.txt
```

Then start the proxy:
```shell
python3 proxy.py
```

## Usage
Once Rateflex is up and running, you can use it by appending `http://localhost:5000` to your original API requests. For example, if your original request is:
```shell
curl https://api.example.com/users
```
Your new request would be like this:
```shell
curl http://localhost:5000/https://api.example.com/users
```

## Why Use Rateflex?

Rateflex is designed to overcome rate limitations imposed by third-party APIs during development. It allows developers to send multiple requests without getting temporarily blocked, which can significantly impact productivity. By caching responses, Rateflex can serve previously fetched data instead of making additional requests to the target API.

## Supported Use Cases

Rateflex is suitable for most API calls. It is primarily focused on handling text-based payloads and may not handle binary responses (e.g., images) as effectively. However, the app may introduce binary support in future updates.

<br/>

---

<br/>

## Contributing 🙌

We welcome contributions to Rateflex! If you have any changes or new features to propose, you can:

* Build the changes yourself and create a pull request (we appreciate it!)
* Create an issue to describe your desired modifications or additions in detail.

## TODO ⏳

* Enhance cache strategies to optimize performance and efficiency (current implementation based on HTTP method and URL)
