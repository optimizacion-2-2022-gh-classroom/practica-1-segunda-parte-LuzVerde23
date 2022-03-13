FROM ubuntu:20.04

ENV TIMEZONE America/Mexico_City
ENV JUPYTERLAB_VERSION 3.2.8
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEB_BUILD_DEPS="build-essential python3-dev python3-pip python3-setuptools software-properties-common libgit2-dev dirmngr libgmp3-dev libmpfr-dev"
ENV DEB_PACKAGES="sudo nano less time git curl wget htop graphviz gfortran libopenblas-dev"
ENV PIP_PACKAGES="numpy scipy matplotlib pandas seaborn sympy cvxpy cvxopt pytest dask distributed bokeh jupyter-book networkx ortools line_profiler memory_profiler psutil guppy3 cython numba graphviz"

#install app debian
RUN apt-get update && export $DEBIAN_FRONTEND && \
    echo $TIMEZONE > /etc/timezone && apt-get install -y tzdata

#install python
RUN apt-get update && apt-get install -y $DEB_BUILD_DEPS $DEB_PACKAGES && pip3 install --upgrade pip

# Install nodejs deps
RUN curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - && apt-get install -y nodejs

# install users
RUN groupadd myuser
RUN useradd myuser -g myuser -m -s /bin/bash
RUN echo 'myuser ALL=(ALL:ALL) NOPASSWD:ALL' | (EDITOR='tee -a' visudo)
RUN echo 'myuser:qwerty' | chpasswd
RUN pip3 install jupyter jupyterlab==$JUPYTERLAB_VERSION
USER myuser

# excecute jypyter and set user and pass
RUN jupyter notebook --generate-config && sed -i "s/# c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" ~/.jupyter/jupyter_notebook_config.py

#install python package
RUN pip3 install $PIP_PACKAGES

#c kernel
RUN sudo chmod gou+wrx -R /usr/local/share/jupyter/kernels/
RUN python_version=$(ls ~/.local/lib/|grep python) && pip3 install --user git+https://github.com/brendan-rius/jupyter-c-kernel.git && python3 ~/.local/lib/$python_version/site-packages/jupyter_c_kernel/install_c_kernel --prefix=/usr/local/


RUN sudo chmod gou+wx -R ~/.local

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser"]
