"""Group similar pending questions.
Logic: embed message -> max cosine vs each pending group's messages
-> join best group if score >= threshold, else start a new group."""
