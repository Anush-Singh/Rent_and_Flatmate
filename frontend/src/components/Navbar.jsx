import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav
            style={{
                background: "#1976d2",
                padding: "15px",
                display: "flex",
                gap: "20px"
            }}
        >
            <Link style={{color:"white"}} to="/">Home</Link>

            <Link style={{color:"white"}} to="/register">Register</Link>

            <Link style={{color:"white"}} to="/login">Login</Link>

            <Link style={{color:"white"}} to="/listings">Listings</Link>

            <Link style={{color:"white"}} to="/add-listing">Add Listing</Link>
        </nav>
    );
}