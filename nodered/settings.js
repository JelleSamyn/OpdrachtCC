// settings.js

module.exports = {
    // … standaard settings

    functionGlobalContext: {
        INFLUX_URL: process.env.INFLUX_URL,
        INFLUX_TOKEN: process.env.INFLUX_TOKEN,
        INFLUX_ORG: process.env.INFLUX_ORG,
        INFLUX_BUCKET: process.env.INFLUX_BUCKET
    }
};
