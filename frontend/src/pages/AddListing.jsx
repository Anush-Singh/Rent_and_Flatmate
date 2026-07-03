import { useState } from "react";
import api from "../api/api";

export default function AddListing() {

    const [ownerId, setOwnerId] = useState("");
    const [location, setLocation] = useState("");
    const [rent, setRent] = useState("");
    const [availableFrom, setAvailableFrom] = useState("");
    const [roomType, setRoomType] = useState("");
    const [furnishingStatus, setFurnishingStatus] = useState("");

    const addListing = async () => {

        try {

            const res = await api.post("/listings/", {

                owner_id: Number(ownerId),
                location,
                rent: Number(rent),
                available_from: availableFrom,
                room_type: roomType,
                furnishing_status: furnishingStatus

            });

            alert(res.data.message);

            setOwnerId("");
            setLocation("");
            setRent("");
            setAvailableFrom("");
            setRoomType("");
            setFurnishingStatus("");

        }

        catch (err) {

            console.log(err);

            alert("Failed to add listing");

        }

    };

    return (

        <div style={{ padding: 30 }}>

            <h2>Add Listing</h2>

            <input
                placeholder="Owner ID"
                value={ownerId}
                onChange={(e)=>setOwnerId(e.target.value)}
            />

            <br /><br />

            <input
                placeholder="Location"
                value={location}
                onChange={(e)=>setLocation(e.target.value)}
            />

            <br /><br />

            <input
                placeholder="Rent"
                value={rent}
                onChange={(e)=>setRent(e.target.value)}
            />

            <br /><br />

            <input
                type="date"
                value={availableFrom}
                onChange={(e)=>setAvailableFrom(e.target.value)}
            />

            <br /><br />

            <input
                placeholder="Room Type"
                value={roomType}
                onChange={(e)=>setRoomType(e.target.value)}
            />

            <br /><br />

            <input
                placeholder="Furnishing Status"
                value={furnishingStatus}
                onChange={(e)=>setFurnishingStatus(e.target.value)}
            />

            <br /><br />

            <button onClick={addListing}>
                Add Listing
            </button>

        </div>

    );
}