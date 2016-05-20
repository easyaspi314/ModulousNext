(function() {
  var dragNop, error, get, loading, selectFile, valid, zipFile;

  zipFile = null;

  loading = false;

  valid = true;

  get = function(name) {
    console.log(name)
    return document.getElementById(name).value;
  };

  error = function(name) {
    console.log(name)
    document.getElementById(name).parentElement.classList.add('has-error');
    document.getElementById('error-alert').classList.remove('hidden');
    return valid = false;
  };

  document.getElementById('submit').addEventListener('click', function() {
    var a, ckan, form, game, gameVersion, i, len, license, link, progress, ref, shortDescription, version, xhr;
    ref = document.querySelectorAll('.has-error');
    for (i = 0, len = ref.length; i < len; i++) {
      a = ref[i];
      a.classList.remove('has-error');
    }
    document.getElementById('error-alert').classList.add('hidden');
    valid = true;
    link = get('mod-link');
    license = get('mod-license');
    if (license === 'Other') {
      license = get('mod-other-license');
    }
    version = get('mod-version');
    gameVersion = get('mod-game-version');
    game = get('mod-game');
    if (link === '') {
      error('mod-link');
    }
    if (license === '') {
      error('mod-license');
    }
    if (version === '') {
      error('mod-version');
    }
    progress = document.getElementById('progress');
    xhr = new XMLHttpRequest();
    xhr.onload = function() {
  var alert, result;
  if (this.statusCode === 502) {
    result = {
      error: true,
      message: "This mod is too big to upload. Contact support@spacedock.info"
    };
  } else {
    result = JSON.parse(this.responseText);
  }
    progress.classList.remove('active');
    if (result.error == null) {
      return window.location = JSON.parse(this.responseText).url;
    } else {
      alert = document.getElementById('error-alert');
      alert.classList.remove('hidden');
      alert.textContent = result.reason;
      document.getElementById('submit').removeAttribute('disabled');
      return loading = false;
      }
    };
    xhr.open('POST', '/api/mod/import_gb');
    form = new FormData();
    form.append('game', game);
    form.append('license', license);
    form.append('version', version);
    form.append('game-version', gameVersion);
    form.append('link', link);
    document.getElementById('submit').setAttribute('disabled', 'disabled');
    progress.querySelector('.progress-bar').style.width = '0%';
    progress.classList.add('active');
    return xhr.send(form);
  }, false);

  $('#mod-license').chosen().change(function() {
    var license;
    license = void 0;
    license = get('mod-license');
    if (license === 'Other') {
      return document.getElementById('mod-other-license').classList.remove('hidden');
    } else {
      return document.getElementById('mod-other-license').classList.add('hidden');
    }
  });

  selectFile = function(file) {
    var p, parent;
    zipFile = file;
    parent = document.querySelector('.upload-mod');
    parent.querySelector('a').classList.add('hidden');
    p = document.createElement('p');
    p.textContent = 'Ready.';
    return parent.appendChild(p);
  };

  document.querySelector('.upload-mod a').addEventListener('click', function(e) {
    e.preventDefault();
    return document.querySelector('.upload-mod input').click();
  }, false);

  document.querySelector('.upload-mod input').addEventListener('change', function(e) {
    return selectFile(e.target.files[0]);
  }, false);

  dragNop = function(e) {
    e.stopPropagation();
    return e.preventDefault();
  };

  window.addEventListener('dragenter', dragNop, false);

  window.addEventListener('dragleave', dragNop, false);

  window.addEventListener('dragover', dragNop, false);

  window.addEventListener('drop', function(e) {
    dragNop(e);
    return selectFile(e.dataTransfer.files[0]);
  }, false);

  document.getElementById('submit').removeAttribute('disabled');

  $('[data-toggle="tooltip"]').tooltip();

}).call(this);
