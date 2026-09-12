const localtunnel = require('localtunnel');

async function startTunnel() {
  try {
    const tunnel = await localtunnel({ port: 3000, subdomain: 'smartqueue-live-demo-now' });
    console.log(`Your public URL is: ${tunnel.url}`);

    tunnel.on('close', () => {
      console.log('Tunnel closed. Reconnecting...');
      setTimeout(startTunnel, 2000);
    });
  } catch (err) {
    console.log('Error:', err);
    setTimeout(startTunnel, 2000);
  }
}

startTunnel();
