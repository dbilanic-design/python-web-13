@app.get("/verify/{token}")
def verify_email(token: str, db: Session = Depends(get_db)):
    user = decode_token(token)
    db_user = db.query(User).get(user["sub"])
    db_user.is_verified = True
    db.commit()
    return {"message": "Email verified"}
