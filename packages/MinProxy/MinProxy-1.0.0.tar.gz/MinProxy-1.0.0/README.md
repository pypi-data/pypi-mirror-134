#MinProxy
Thư viện viết lên bởi Tài Lê :DD
Đây là thư viện tự động lấy proxy của website Minproxy.vn
Khi nhập apikey của MinProxy
Thư viện sẽ tự động check type của api key và trả về IP và Port
Nhập API Key V4 hay V6 đều được

## Requirments
Hưỡng dẫn sử dụng thư viện Minproxy
Các lệnh - Command Line Python

Import thư viện
```bash
import MinProxy
```

Lấy thông tin API Key

import by from
```bash
from MinProxy import CheckApiKey
```

Sử dụng 'CheckApiKey' với tham 'số api_key'
```bash
CheckApiKey(api_key='your api key by minproxy.vn')
```

Code Example
```bash
import MinProxy
from MinProxy import CheckApiKey

api_key="Key IPG6 hoặc V4"
CheckApiKey(api_key=api_key)
```


Get Proxy
import
```bash
from MinProxy import Get_Proxy
```

Sử dụng 'Get_Proxy' với tham số là 'your_api_key'
```bash
Get_Proxy(api_key='your api key')
```

Code Example
```bash
import MinProxy
from MinProxy import Get_Proxy

api_key="Key IPG6 hoặc V4"
Get_Proxy(api_key=api_key)
```