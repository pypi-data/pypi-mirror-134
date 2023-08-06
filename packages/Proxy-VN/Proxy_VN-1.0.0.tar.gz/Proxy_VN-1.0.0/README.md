## Proxy_Việt Nam
Thư viện viết lên bởi Tài Lê :DD
Đây là thư viện tự động lấy proxy của website Minproxy.vn và Tmproxy.com
Khi nhập apikey thư viện sẽ tự động check type của api key và trả về IP và Port
Nhập API Key

## Requirments
Hưỡng dẫn sử dụng thư viện Minproxy
Các lệnh - Command Line Python

Import thư viện
```bash
import Proxy_VN
```

Lấy thông tin API Key

# MinProxy
```bash
from Proxy_VN import Min
```

Sử dụng 'CheckApiKey' với tham 'số api_key'
```bash
Min.CheckApiKey(api_key='your api key by minproxy.vn')
```

Code Example
```bash
import Proxy_VN
from Proxy_VN import Min

api_key="Key IPG6 hoặc V4"
Min.CheckApiKey(api_key=api_key)
```


# Lấy IP:Port
Sử dụng 'Get_Proxy' với tham số là 'your_api_key'
```bash
Min.Get_Proxy(api_key='your api key')
```

# Code Example
```bash
import Proxy_VN
from Proxy_VN import Min

api_key="Key IPG6 hoặc V4"
Min.Get_Proxy(api_key=api_key)
```




# TMProxy
```bash
from Proxy_VN import TM
```

Sử dụng 'CheckApiKey' với tham 'số api_key'
```bash
TM.CheckApiKey(api_key='your api key by minproxy.vn')
```

Code Example
```bash
import Proxy_VN
from Proxy_VN import TM

api_key="Key IPG6 hoặc V4"
TM.CheckApiKey(api_key=api_key)
```


# Lấy IP:Port
Sử dụng 'Get_Proxy' với tham số là 'your_api_key'
```bash
TM.Get_Proxy(api_key='your api key')
```

# Code Example
```bash
import Proxy_VN
from Proxy_VN import TM

api_key="Key IPG6 hoặc V4"
TM.Get_Proxy(api_key=api_key)
```