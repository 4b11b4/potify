module.exports = {
/*  configureWebpack: {
    module: {
      rules: [
        {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options:
            {
              implementation: require('sass'),
              sassOptions:
              {
                indentedSyntax: true
              }	
            }
          }
        ]}
      ]
    }
  },
*/
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://127.0.0.1:8000/',
        ws: false,
      }
    }
  },
  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: './dist/',
  // assetsDir must match Django's STATIC_URL
  assetsDir: 'static',
}

