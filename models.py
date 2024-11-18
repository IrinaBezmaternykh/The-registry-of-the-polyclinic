from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class Patient(Base):
    __tablename__ = 'Пациенты'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    patrname = Column(String(50), nullable=True)
    oms = Column(String(16), nullable=False)
    birthday = Column(String(8), nullable=False)
    sex = Column(String(1), nullable=False)
    adress = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)

    def __repr__(self):
        return f'<Patient {self.lastname!r}>'


class Doctor(Base):
    __tablename__ = 'Врачи'
    id = Column(Integer, primary_key=True)
    lastname = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    patrname = Column(String(50), nullable=True)
    spec = Column(String(50), nullable=False)
    cab = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Doctor {self.lastname!r}>'


class Appointment(Base):
    __tablename__ = 'Приемы'
    id = Column(Integer, primary_key=True)
    appdate = Column(String(8), nullable=False)
    apptime = Column(String(5), nullable=False)
    problem = Column(String(255), nullable=True)
    patient_id = Column(Integer, ForeignKey('Пациенты.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('Врачи.id'), nullable=False)

    def __repr__(self):
        return f'<Appointment {self.id!r}>'
