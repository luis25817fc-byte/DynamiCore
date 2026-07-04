import { useState } from "react";
import { sendMessage } from "./api";

export default function App() {
  const [input, setInput] = useState("");
  const [chat, setChat] = useState([]);

  const send = async () => {
    if (!input.trim()) return;

    const msg = input;

    setChat(prev => [...prev, { role: "user", text: msg }]);
    setInput("");

    const res = await sendMessage(msg);

    setChat(prev => [
      ...prev,
      { role: "ai", text: res.response || res.error || "Sin respuesta" }
    ]);
  };

  return (
    <div className="container">
      <h1>DynamiCore AI</h1>

      <div className="chat">
        {chat.map((m, i) => (
          <div key={i} className={m.role}>
            <b>{m.role}:</b> {m.text}
          </div>
        ))}
      </div>

      <div className="inputBox">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Escribe un mensaje..."
        />
        <button onClick={send}>Enviar</button>
      </div>
    </div>
  );
          }
