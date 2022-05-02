const path = require('path');

module.exports = {
    resolve: {
        extensions: ['js', 'ts'], alias: {
            '@': path.resolve(__dirname, 'src'),
            '@assets': path.resolve(__dirname, 'src/assets'),
            '@components': path.resolve(__dirname, 'src/components'),
            '@services': path.resolve(__dirname, 'src/services'),
            '@store': path.resolve(__dirname, 'src/store'),
            '@views': path.resolve(__dirname, 'src/views'),
        },
    },
}