import { useState } from "react";
import api from "../api/api";

export default function Register() {

    const [full_name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const register = async () => {

        try {

            const res = await api.post("/auth/register", {
                full_name,
                email,
                password,
                role: "tenant"
            });

            alert(res.data.message);

            setName("");
            setEmail("");
            setPassword("");

        }

        catch (err) {

            console.log(err);

            alert("Registration Failed");

        }

    }

    return (

        <div style={{ padding: 30 }}>

            <h2>Register</h2>

            <input
                value={full_name}
                placeholder="Full Name"
                onChange={(e) => setName(e.target.value)}
            />

            <br /><br />

            <input
                value={email}
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
            />

            <br /><br />

            <input
                value={password}
                type="password"
                placeholder="Password"
                onChange={(e) => setPassword(e.target.value)}
            />

            <br /><br />

            <button onClick={register}>
                Register
            </button>

        </div>

    )

}