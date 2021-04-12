# To automate the task of creating a custom HTTP header response with Puppet
# https://pptr.dev/#?product=Puppeteer&version=v5.2.1&show=api-pagesetextrahttpheadersheaders

page.setExtraHTTPHeaders([['X-Served-By', '@hostname'],]);
