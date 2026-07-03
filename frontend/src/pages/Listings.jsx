import { useEffect, useState } from "react";
import api from "../api/api";

export default function Listings() {

    const [listings, setListings] = useState([]);

    useEffect(() => {

        fetchListings();

    }, []);

    const fetchListings = async () => {

        const res = await api.get("/listings");

        setListings(res.data);

    }

    return (

        <div style={{ padding: 30 }}>

            <h2>Available Listings</h2>

            {

                listings.map(item => (

                    <div
                        key={item.id}
                        style={{
                            border: "1px solid gray",
                            margin: 20,
                            padding: 20
                        }}
                    >

                        <h3>{item.location}</h3>

                        <p>Rent : ₹{item.rent}</p>

                        <p>{item.room_type}</p>

                    </div>

                ))

            }

        </div>

    )

}