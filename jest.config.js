module.exports = {
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/main/webapp/$1',
    '^~/(.*)$': '<rootDir>/src/main/webapp/$1',
    '^vue$': 'vue/dist/vue.common.js'
  },
  moduleFileExtensions: ['js', 'vue', 'json'],
  transform: {
    '^.+\\.js$': 'babel-jest',
    '.*\\.(vue)$': 'vue-jest'
  },
  'collectCoverage': true,
  'collectCoverageFrom': [
    '<rootDir>/src/main/webapp/components/**/*.vue',
    '<rootDir>/src/main/webapp/pages/**/*.vue'
  ]
}
