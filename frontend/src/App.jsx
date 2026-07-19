import { useState } from "react";
import { sendMessage } from "./api";

export default function App() {
  const [input, setInput] = useState("");
  const [chat, setChat] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const msg = input;
    setInput("");

    setChat(prev => [...prev, { role: "user", text: msg }]);

    try {
      const res = await sendMessage(msg);

      setChat(prev => [
        ...prev,
        {
          role: "ai",
          text: res?.response || res?.error || "Sin respuesta"
        }
      ]);
    } catch (err) {
      setChat(prev => [
        ...prev,
        { role: "ai", text: "Error frontend: " + err.message }
      ]);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>DynamiCore AI</h1>

      {chat.map((m, i) => (
        <div key={i}>
          <b>{m.role}:</b> {m.text}
        </div>
      ))}

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={handleSend}>Enviar</button>
    </div>
  );
        }
