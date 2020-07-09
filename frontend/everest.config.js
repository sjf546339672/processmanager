module.exports = {
  pages: {
    index: {
      entry: './src/index.js',
      template: './public/index.html'
    }
  },
  themes: ['white', 'blue'],
  alias: {
    '@': './src'
  },
  proxy: [
    {
      context: [
        '/api/**',
        '/tenant/**',
        '/notify/**',
        '/portal/**',
        '/userrole/**',
        '/frontend/**'
      ],
      target: 'http://10.1.62.146'
    },
    {
      context: ['/processmanger/frontapi/v1'],
      // target: 'http://127.0.0.1:9770/'
      target: 'http://127.0.0.1:9005/'
    }
  ]
}
