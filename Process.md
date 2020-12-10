process
=======

- install swagger

    brew install swagger

```
For the system Java wrappers to find this JDK, symlink it with
  sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk is keg-only, which means it was not symlinked into /usr/local,
because it shadows the macOS `java` wrapper.

If you need to have openjdk first in your PATH run:
  echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> ~/.zshrc

For compilers to find openjdk you may need to set:
  export CPPFLAGS="-I/usr/local/opt/openjdk/include"
```

- generate code 

  swagger-codegen -i [/path/to/swagger](https://help.rapid7.com/insightvm/en-us/api/api.json) -l python

- install said package 

    pip install -e .

- learn [swagger](https://mjstealey.github.io/swagger-demo/pythonclient/) and python

    /me goes to the internet

- create user with api auth key

    https://insight.rapid7.com/platform#/apiKeyManagement/user