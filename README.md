[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/avmmodules/AVMWeather">
    <img src="https://raw.githubusercontent.com/avmmodules/AVMWeather/main/img/logo.png" alt="Logo" width="300">
  </a>

  <h3 align="center">AVMWeather</h3>

  <p align="center">
    Get weather data in a simple way!
    <br />
    <a href="https://github.com/avmmodules/AVMWeather"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/avmmodules/AVMWeather/issues">Report Bug</a>
    ·
    <a href="https://github.com/avmmodules/AVMWeather/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![miniatura][miniatura]](https://pypi.org/project/AVMWeather/)

If you want to watch the explanation in video, see the [link](https://www.youtube.com/avmmodules)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to make sure you have installed the following modules.
* Requests
  ```s
  pip install requests
  ```

### Installation

```python
pip install AVMWeather
```

<!-- USAGE EXAMPLES -->
## Usage

* Example 1
    ```python
    import AVMWeather as weather

    lat = '34.399230' # latitude
    lon = '104.075223' # longitude
    api = 'YOUR_API_KEY_HERE' # your api key

    res = weather.get_weather(lat, lon, api)
    print(res) # prints all weather's info of Asia/Shangai
    ```

_For more examples, please refer to the [Examples packages](https://github.com/avmmodules/AVMWeather/tree/main/examples)_

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/avmmodules/AVMWeather/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Youtube: [/avmmodules](https://youtube.com/avmmodules)

Email: avmmodules@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/avmmodules/AVMWeather.svg?style=for-the-badge
[contributors-url]: https://github.com/avmmodules/AVMWeather/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/avmmodules/AVMWeather.svg?style=for-the-badge
[forks-url]: https://github.com/avmmodules/AVMWeather/network/members
[stars-shield]: https://img.shields.io/github/stars/avmmodules/AVMWeather.svg?style=for-the-badge
[stars-url]: https://github.com/avmmodules/AVMWeather/stargazers
[issues-shield]: https://img.shields.io/github/issues/avmmodules/AVMWeather.svg?style=for-the-badge
[issues-url]: https://github.com/avmmodules/AVMWeather/issues
[license-shield]: https://img.shields.io/github/license/avmmodules/AVMWeather.svg?style=for-the-badge
[license-url]: https://github.com/avmmodules/AVMWeather/blob/main/LICENSE
[miniatura]: https://raw.githubusercontent.com/avmmodules/AVMWeather/main/img/miniatura.png
