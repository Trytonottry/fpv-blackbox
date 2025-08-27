window.BETAFLIGHT.plugins.fpvAnalyzer = {
  initialize: function (tab) {
    $('#content').append(`
      <div id="fpv-analyzer">
        <h3>FPV Blackbox Analyzer</h3>
        <button id="upload-flight">Upload to Cloud</button>
      </div>
    `);

    $('#upload-flight').click(() => {
      const log = getCurrentLog();
      fetch('https://api.fpvanalyzer.dev/api/upload', {
        method: 'POST',
        body: log
      });
    });
  }
};