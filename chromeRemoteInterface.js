const CDP = require('chrome-remote-interface');

CDP(async (client) => {
    const { Network, Page, Runtime } = client;
    try {
        await Promise.all([Network.enable(), Page.enable(), Runtime.enable()]);

        Runtime.consoleAPICalled(({ args, type }) => {
            args.forEach(arg => {
                // Write logs to a file or process them as needed
                console.log(`${type}: ${arg.value}`);
            });
        });

        await Page.navigate({ url: 'http://github.com/tsrctester1/demo/pulls' });
        await Page.loadEventFired();
    } catch (err) {
        console.error(err);
    } finally {
        client.close();
    }
}).on('error', (err) => {
    console.error(`Cannot connect to browser: ${err}`);
});
