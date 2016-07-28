import WebSocket from 'reconnecting-websocket';
import biu from 'biu.js';

function addNotification(data) {
  const result = JSON.parse(data);
  if (window.Notification && Notification.permission === 'granted') {
    const body = `New message: ${result.content}\nFrom: ${result.sender_name}`;
    const note = new Notification('apostello', { body });
    note.onclick = () => {
      document.location = '/';
    };
  } else {
    biu(
      `${result.sender_name}: ${result.content}`,
      { type: 'success', timeout: 5000 }
    );
  }
}

window.addEventListener('load', () => {
  Notification.requestPermission((status) => {
    if (Notification.permission !== status) {
      Notification.permission = status;
    }
  });
});

function renderNotifications() {
  const wsScheme = window.location.protocol === 'https:' ? 'wss' : 'ws';
  const wsUrl = `${wsScheme}://${window.location.host}/`;
  const ws = new WebSocket(wsUrl);
  ws.addEventListener('message', (message) => {
    addNotification(message.data);
  });
}

export { renderNotifications };
