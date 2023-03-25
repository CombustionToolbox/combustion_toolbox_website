<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8SBZV15K7W"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-8SBZV15K7W');
</script>

<!-- Organize Website -->
```{toctree}
   :hidden:

Home <self>
```

```{toctree}
    :hidden:
    :maxdepth: 2
    :titlesonly:

install
tutorial
examples
validations
publications
```

<!-- Include home -->

```{include} home.md
:relative-images:
```

<!-- Include documentation -->

```{toctree}
    :caption: 'Documentation'
    :hidden:
    :maxdepth: 2
    :titlesonly:

documentation/index
documentation/databases
documentation/functions/index
```